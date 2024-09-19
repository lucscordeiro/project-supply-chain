import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../api'; // Ajuste o caminho conforme necessário

const Home = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const loadProducts = async () => {
            const fetchedProducts = await fetchProducts();
            setProducts(fetchedProducts); // Atualiza o estado com os produtos
        };
        loadProducts();
    }, []);

    return (
        <div>
            {products.length > 0 ? (
                products.map(product => (
                    <div key={product.id}>{product.name}</div> // Ajuste conforme a estrutura do seu produto
                ))
            ) : (
                <p>No products found</p>
            )}
        </div>
    );
};

export default Home;
