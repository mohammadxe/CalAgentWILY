import { useState, useCallback } from 'react';
import { Alert } from 'react-native';
import { Product, AutomationStatus } from '../types';

interface UseAutomationReturn {
  startAutomation: (products: Product[], deviceType: 'ios' | 'android') => Promise<void>;
  status: AutomationStatus['status'];
  message: string;
  progress: number;
  isRunning: boolean;
}

export function useAutomation(apiBaseUrl: string): UseAutomationReturn {
  const [status, setStatus] = useState<AutomationStatus['status']>('idle');
  const [message, setMessage] = useState('');
  const [progress, setProgress] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  const startAutomation = useCallback(async (products: Product[], deviceType: 'ios' | 'android') => {
    setIsRunning(true);
    setStatus('connecting');
    setMessage('Connecting to automation service...');
    setProgress(0);

    try {
      // Use WebSocket for real-time updates
      const wsUrl = apiBaseUrl.replace('http', 'ws') + '/ws/automate';
      const ws = new WebSocket(wsUrl);

      ws.onopen = () => {
        console.log('WebSocket connected');
        ws.send(JSON.stringify({
          products,
          device_type: deviceType,
        }));
      };

      ws.onmessage = (event) => {
        try {
          const data: AutomationStatus = JSON.parse(event.data);
          setStatus(data.status);
          setMessage(data.message);
          setProgress(data.progress);

          if (data.status === 'completed') {
            Alert.alert('Success', data.message);
            setIsRunning(false);
            ws.close();
          } else if (data.status === 'error') {
            Alert.alert('Error', data.message);
            setIsRunning(false);
            ws.close();
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        Alert.alert('Connection Error', 'Failed to connect to automation service. Make sure the backend is running on your MacBook.');
        setIsRunning(false);
        setStatus('error');
        setMessage('Connection failed');
      };

      ws.onclose = () => {
        console.log('WebSocket closed');
        // Check current status instead of captured status
        setStatus((currentStatus) => {
          if (currentStatus !== 'completed' && currentStatus !== 'error') {
            setIsRunning(false);
            return 'idle';
          }
          return currentStatus;
        });
      };

      // Fallback: Use HTTP if WebSocket fails
      setTimeout(() => {
        if (ws.readyState !== WebSocket.OPEN) {
          console.log('WebSocket not ready, trying HTTP fallback');
          startAutomationHTTP(products, deviceType);
        }
      }, 3000);

    } catch (error) {
      console.error('Automation error:', error);
      Alert.alert('Error', `Failed to start automation: ${error}`);
      setIsRunning(false);
      setStatus('error');
      setMessage('Failed to start automation');
    }
  }, [apiBaseUrl]);

  const startAutomationHTTP = async (products: Product[], deviceType: 'ios' | 'android') => {
    try {
      const response = await fetch(`${apiBaseUrl}/automate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          products,
          device_type: deviceType,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setStatus(data.status);
      setMessage(data.message);
      setProgress(100);
      
      if (data.status === 'completed') {
        Alert.alert('Success', data.message);
      }
    } catch (error) {
      console.error('HTTP automation error:', error);
      Alert.alert('Error', `Failed to start automation: ${error}`);
      setStatus('error');
      setMessage('Failed to start automation');
    } finally {
      setIsRunning(false);
    }
  };

  return {
    startAutomation,
    status,
    message,
    progress,
    isRunning,
  };
}

