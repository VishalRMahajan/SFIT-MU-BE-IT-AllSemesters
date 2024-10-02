import React from 'react';
import './Sessions.css';

function Sessions() {
  return (
    <div className="sessions-container">
      <h2>Web Development Topics</h2>

      <section className="section-box">
        <h3>1. HTML</h3>
        <p>
          HTML (HyperText Markup Language) is the backbone of any web page. It provides the structure of a webpage by using elements such as headings, paragraphs, links, and images. It forms the foundation of all web development.
        </p>
      </section>

      <section className="section-box">
        <h3>2. CSS</h3>
        <p>
          CSS (Cascading Style Sheets) is used to style and layout web pages. It allows developers to add colors, fonts, and spacing, and control how elements are displayed on different devices. CSS enables responsive design and improves user experience.
        </p>
      </section>

      <section className="section-box">
        <h3>3. JavaScript</h3>
        <p>
          JavaScript is a powerful programming language that enables interactivity on websites. From form validation to complex animations and asynchronous data fetching, JavaScript makes websites dynamic and interactive.
        </p>
      </section>

      <section className="section-box">
        <h3>4. React</h3>
        <p>
          React is a popular JavaScript library for building user interfaces, especially for single-page applications. It helps developers create reusable components, making the code more manageable and efficient.
        </p>
      </section>

      <section className="section-box">
        <h3>5. Node.js</h3>
        <p>
          Node.js is a server-side runtime environment that allows JavaScript to be used on the server. It is known for its efficiency and scalability, making it ideal for building fast, data-intensive applications.
        </p>
      </section>
    </div>
  );
}

export default Sessions;
