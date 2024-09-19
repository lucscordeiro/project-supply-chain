import React, { useState } from 'react';
import axios from 'axios';

const TrackProduct = () => {
    const [productID, setProductID] = useState('');
    const [productData, setProductData] = useState(null);

    const handleTrackProduct = () => {
        axios.get(`http://localhost:5000/products/${productID}`)
            .then(response => setProductData(response.data))
            .catch(error => console.error('Error:', error));
    };

    return (
        <div>
            <h2>Track Product</h2>
            <input 
                type="text" 
                value={productID} 
                onChange={e => setProductID(e.target.value)} 
                placeholder="Product ID" 
            />
            <button onClick={handleTrackProduct}>Track Product</button>
            {productData && (
                <div>
                    <h3>Product Details</h3>
                    <p><strong>ID:</strong> {productData.product.id}</p>
                    <p><strong>Name:</strong> {productData.product.name}</p>
                    <p><strong>Description:</strong> {productData.product.description}</p>
                    <p><strong>Supplier:</strong> {productData.product.supplier}</p>
                    <p><strong>Location:</strong> {productData.product.location}</p>
                    <h4>Stages</h4>
                    <ul>
                        {productData.stages.map((stage, index) => (
                            <li key={index}>
                                <p><strong>Date and Time:</strong> {new Date(stage.date_time).toLocaleString()}</p>
                                <p><strong>Location:</strong> {stage.location}</p>
                                <p><strong>Responsible:</strong> {stage.responsible}</p>
                                <p><strong>Additional Info:</strong> {stage.additional_info}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default TrackProduct;
