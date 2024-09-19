import React, { useState } from 'react';
import axios from 'axios';

const AddProduct = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [supplier, setSupplier] = useState('');
    const [location, setLocation] = useState('');

    const handleAddProduct = () => {
        axios.post('http://localhost:5000/products', { name, description, supplier, location })
            .then(response => alert(response.data.message))
            .catch(error => console.error('Error:', error));
    };

    return (
        <div>
            <h2>Add Product</h2>
            <input 
                type="text" 
                value={name} 
                onChange={e => setName(e.target.value)} 
                placeholder="Product Name" 
            />
            <input 
                type="text" 
                value={description} 
                onChange={e => setDescription(e.target.value)} 
                placeholder="Description" 
            />
            <input 
                type="text" 
                value={supplier} 
                onChange={e => setSupplier(e.target.value)} 
                placeholder="Supplier" 
            />
            <input 
                type="text" 
                value={location} 
                onChange={e => setLocation(e.target.value)} 
                placeholder="Location" 
            />
            <button onClick={handleAddProduct}>Add Product</button>
        </div>
    );
};

export default AddProduct;
