import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';

interface AutomationControlProps {
  onStart: () => void;
  status: string;
  progress: number;
  isRunning: boolean;
  productCount: number;
}

export function AutomationControl({
  onStart,
  status,
  progress,
  isRunning,
  productCount,
}: AutomationControlProps) {
  const getStatusColor = () => {
    switch (status) {
      case 'completed':
        return '#27ae60';
      case 'error':
        return '#e74c3c';
      case 'connecting':
      case 'connected':
      case 'navigating':
      case 'adding_product':
        return '#3498db';
      default:
        return '#7f8c8d';
    }
  };

  const getStatusMessage = () => {
    if (isRunning) {
      switch (status) {
        case 'connecting':
          return 'Connecting to device...';
        case 'connected':
          return 'Device connected';
        case 'navigating':
          return 'Navigating app...';
        case 'adding_product':
          return 'Adding products...';
        case 'completed':
          return 'Completed successfully!';
        case 'error':
          return 'Error occurred';
        default:
          return 'Running...';
      }
    }
    return 'Ready to start';
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Automation Control</Text>
      
      {isRunning && (
        <View style={styles.statusContainer}>
          <View style={styles.statusBar}>
            <View
              style={[
                styles.progressBar,
                { width: `${progress}%`, backgroundColor: getStatusColor() },
              ]}
            />
          </View>
          <View style={styles.statusInfo}>
            <ActivityIndicator
              size="small"
              color={getStatusColor()}
              style={styles.spinner}
            />
            <Text style={[styles.statusText, { color: getStatusColor() }]}>
              {getStatusMessage()}
            </Text>
            <Text style={styles.progressText}>{Math.round(progress)}%</Text>
          </View>
        </View>
      )}

      <TouchableOpacity
        style={[
          styles.startButton,
          (isRunning || productCount === 0) && styles.startButtonDisabled,
        ]}
        onPress={onStart}
        disabled={isRunning || productCount === 0}
      >
        {isRunning ? (
          <ActivityIndicator color="#ffffff" />
        ) : (
          <Text style={styles.startButtonText}>
            {productCount === 0 ? 'Add Products First' : 'Start Automation'}
          </Text>
        )}
      </TouchableOpacity>

      {productCount > 0 && !isRunning && (
        <Text style={styles.hint}>
          Will add {productCount} product{productCount !== 1 ? 's' : ''} to Albert Heijn basket
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 24,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#34495e',
    marginBottom: 16,
  },
  statusContainer: {
    marginBottom: 20,
  },
  statusBar: {
    height: 8,
    backgroundColor: '#ecf0f1',
    borderRadius: 4,
    overflow: 'hidden',
    marginBottom: 12,
  },
  progressBar: {
    height: '100%',
    borderRadius: 4,
    transition: 'width 0.3s ease',
  },
  statusInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  spinner: {
    marginRight: 4,
  },
  statusText: {
    flex: 1,
    fontSize: 14,
    fontWeight: '500',
  },
  progressText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#7f8c8d',
  },
  startButton: {
    backgroundColor: '#3498db',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 56,
  },
  startButtonDisabled: {
    backgroundColor: '#bdc3c7',
  },
  startButtonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: '600',
  },
  hint: {
    marginTop: 12,
    fontSize: 12,
    color: '#7f8c8d',
    textAlign: 'center',
  },
});

