// src/components/ProductDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchProductDetails } from '../api';

const ProductDetails = () => {
  const { productId } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const loadProductDetails = async () => {
      const data = await fetchProductDetails(productId);
      setProduct(data);
    };
    loadProductDetails();
  }, [productId]);

  if (!product) return <div>Loading...</div>;

  return (
    <div>
      <h1>{product.name}</h1>
      <p>Origem: {product.origin}</p>
      {/* Adicione outras informações necessárias */}
    </div>
  );
};

export default ProductDetails;
