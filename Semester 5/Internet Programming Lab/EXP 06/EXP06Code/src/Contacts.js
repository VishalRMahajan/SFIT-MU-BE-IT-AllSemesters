import React from 'react';
import './Contacts.css';

function Contacts() {
  return (
    <div className="contact-container">
      <div className="contact-box">
        <h2>Contact Us</h2>
        <p><strong>Phone:</strong> +91-12345-67890</p>
        <p><strong>Email:</strong> <a href="mailto:example@example.com">vism06@student.sfit.ac.in</a></p>
        <p><strong>Address:</strong> Gate no 5, SFIMAR, Mount Poinsur, S.V.P Road, Borivali(W)-400103</p>
      </div>
    </div>
  );
}

export default Contacts;
