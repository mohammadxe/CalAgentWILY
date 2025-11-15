import React, { useState } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  Alert,
  ActivityIndicator,
  ScrollView,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { ProductList } from './components/ProductList';
import { AutomationControl } from './components/AutomationControl';
import { useAutomation } from './hooks/useAutomation';
import { Product } from './types';

// IMPORTANT: Replace with your MacBook's IP address
// Find it by: System Preferences > Network > Wi-Fi > Advanced > TCP/IP
// Or run: ifconfig | grep "inet " | grep -v 127.0.0.1
const API_BASE_URL = __DEV__ 
  ? 'http://192.168.1.XXX:8000'  // Replace XXX with your MacBook's IP address
  : 'http://your-server.com:8000';

export default function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [productName, setProductName] = useState('');
  const [deviceType, setDeviceType] = useState<'ios' | 'android'>('ios');
  const { startAutomation, status, progress, isRunning } = useAutomation(API_BASE_URL);

  const addProduct = () => {
    if (productName.trim()) {
      setProducts([...products, { name: productName.trim(), quantity: 1 }]);
      setProductName('');
    }
  };

  const removeProduct = (index: number) => {
    setProducts(products.filter((_, i) => i !== index));
  };

  const updateQuantity = (index: number, quantity: number) => {
    const updated = [...products];
    updated[index].quantity = Math.max(1, quantity);
    setProducts(updated);
  };

  const handleStartAutomation = async () => {
    if (products.length === 0) {
      Alert.alert('No Products', 'Please add at least one product');
      return;
    }

    await startAutomation(products, deviceType);
  };

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        <Text style={styles.title}>Albert Heijn Automation</Text>
        <Text style={styles.subtitle}>Control your shopping automation</Text>

        {/* Device Type Selection */}
        <View style={styles.deviceSection}>
          <Text style={styles.sectionTitle}>Device Type</Text>
          <View style={styles.deviceButtons}>
            <TouchableOpacity
              style={[styles.deviceButton, deviceType === 'ios' && styles.deviceButtonActive]}
              onPress={() => setDeviceType('ios')}
            >
              <Text style={[styles.deviceButtonText, deviceType === 'ios' && styles.deviceButtonTextActive]}>
                iOS
              </Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.deviceButton, deviceType === 'android' && styles.deviceButtonActive]}
              onPress={() => setDeviceType('android')}
            >
              <Text style={[styles.deviceButtonText, deviceType === 'android' && styles.deviceButtonTextActive]}>
                Android
              </Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Add Product */}
        <View style={styles.addProductSection}>
          <Text style={styles.sectionTitle}>Add Product</Text>
          <View style={styles.inputContainer}>
            <TextInput
              style={styles.input}
              placeholder="Enter product name..."
              value={productName}
              onChangeText={setProductName}
              onSubmitEditing={addProduct}
            />
            <TouchableOpacity style={styles.addButton} onPress={addProduct}>
              <Text style={styles.addButtonText}>Add</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Product List */}
        <ProductList
          products={products}
          onRemove={removeProduct}
          onUpdateQuantity={updateQuantity}
        />

        {/* Automation Control */}
        <AutomationControl
          onStart={handleStartAutomation}
          status={status}
          progress={progress}
          isRunning={isRunning}
          productCount={products.length}
        />
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: 20,
    paddingTop: 60,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 8,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#7f8c8d',
    marginBottom: 30,
    textAlign: 'center',
  },
  deviceSection: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#34495e',
    marginBottom: 12,
  },
  deviceButtons: {
    flexDirection: 'row',
    gap: 12,
  },
  deviceButton: {
    flex: 1,
    padding: 14,
    borderRadius: 8,
    backgroundColor: '#ecf0f1',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'transparent',
  },
  deviceButtonActive: {
    backgroundColor: '#3498db',
    borderColor: '#2980b9',
  },
  deviceButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#7f8c8d',
  },
  deviceButtonTextActive: {
    color: '#ffffff',
  },
  addProductSection: {
    marginBottom: 24,
  },
  inputContainer: {
    flexDirection: 'row',
    gap: 10,
  },
  input: {
    flex: 1,
    height: 50,
    backgroundColor: '#ffffff',
    borderRadius: 8,
    paddingHorizontal: 16,
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  addButton: {
    paddingHorizontal: 24,
    height: 50,
    backgroundColor: '#27ae60',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  addButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '600',
  },
});

