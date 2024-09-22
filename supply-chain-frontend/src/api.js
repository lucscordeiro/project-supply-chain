const API_URL = 'http://localhost:5000/api';

export const fetchProducts = async () => {
    try {
        const response = await fetch(`${API_URL}/products`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        
        // Verifica se a resposta é um array
        if (!Array.isArray(data)) {
            console.error("Expected an array but received:", data);
            return []; // Retorna um array vazio se não for um array
        }

        return data; // Retorna o array de produtos
    } catch (error) {
        console.error('Error fetching products:', error);
        return []; // Retorna um array vazio em caso de erro
    }
};

  
export const fetchProductDetails = async (productId) => {
  const response = await fetch(`${API_URL}/products/${productId}`);
  return await response.json();
};

export const fetchTransactions = async () => {
    try {
      const response = await fetch('/api/transactions');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data; // Deve ser um array
    } catch (error) {
      console.error('Error fetching transactions:', error);
      return []; // Retorna um array vazio em caso de erro
    }
  };
  
export const fetchBlockchain = async () => {
    try {
      const response = await fetch('/api/blockchain');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data; // Deve ser um array
    } catch (error) {
      console.error('Error fetching blockchain:', error);
      return []; // Retorna um array vazio em caso de erro
    }
  };

export const createProduct = async (product) => {
  const response = await fetch(`${API_URL}/products`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(product),
  });
  return await response.json();
};
