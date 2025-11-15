export interface Product {
  name: string;
  quantity: number;
}

export interface AutomationStatus {
  status: 'idle' | 'connecting' | 'connected' | 'navigating' | 'adding_product' | 'completed' | 'error';
  message: string;
  progress: number;
  current_product?: string;
}

export interface AutomationRequest {
  products: Product[];
  device_type: 'ios' | 'android';
}

