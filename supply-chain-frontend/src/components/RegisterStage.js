import React, { useState } from 'react';
import axios from 'axios';

const RegisterStage = () => {
    const [productID, setProductID] = useState('');
    const [dateTime, setDateTime] = useState('');
    const [location, setLocation] = useState('');
    const [responsible, setResponsible] = useState('');
    const [additionalInfo, setAdditionalInfo] = useState('');

    const handleRegisterStage = () => {
        axios.post('http://localhost:5000/stages', { 
            product_id: productID,
            date_time: dateTime,
            location,
            responsible,
            additional_info: additionalInfo 
        })
        .then(response => alert(response.data.message))
        .catch(error => console.error('Error:', error));
    };

    return (
        <div>
            <h2>Register Stage</h2>
            <input 
                type="text" 
                value={productID} 
                onChange={e => setProductID(e.target.value)} 
                placeholder="Product ID" 
            />
            <input 
                type="datetime-local" 
                value={dateTime} 
                onChange={e => setDateTime(e.target.value)} 
                placeholder="Date and Time" 
            />
            <input 
                type="text" 
                value={location} 
                onChange={e => setLocation(e.target.value)} 
                placeholder="Location" 
            />
            <input 
                type="text" 
                value={responsible} 
                onChange={e => setResponsible(e.target.value)} 
                placeholder="Responsible" 
            />
            <input 
                type="text" 
                value={additionalInfo} 
                onChange={e => setAdditionalInfo(e.target.value)} 
                placeholder="Additional Info" 
            />
            <button onClick={handleRegisterStage}>Register Stage</button>
        </div>
    );
};

export default RegisterStage;
