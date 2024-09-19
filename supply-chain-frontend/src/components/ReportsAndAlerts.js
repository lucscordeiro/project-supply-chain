import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReportsAndAlerts = () => {
    const [reports, setReports] = useState([]);
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/reports')
            .then(response => setReports(response.data))
            .catch(error => console.error('Error:', error));
        
        axios.get('http://localhost:5000/alerts')
            .then(response => setAlerts(response.data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h2>Reports and Alerts</h2>
            <h3>Reports</h3>
            <ul>
                {reports.map(report => (
                    <li key={report.id}>
                        <p><strong>Title:</strong> {report.title}</p>
                        <p><strong>Details:</strong> {report.details}</p>
                    </li>
                ))}
            </ul>
            <h3>Alerts</h3>
            <ul>
                {alerts.map(alert => (
                    <li key={alert.id}>
                        <p><strong>Message:</strong> {alert.message}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ReportsAndAlerts;
