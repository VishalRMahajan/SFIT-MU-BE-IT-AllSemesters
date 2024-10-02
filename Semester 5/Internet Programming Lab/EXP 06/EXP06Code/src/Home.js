import React from 'react'
import './Home.css'
const Home = () => {
  return (
    <div className='Home'>
      <h3>Topics To Be Covered</h3>
      <table>
        <tr>
          <th>Sr No.</th>
          <th>Topics</th>
         
        </tr>
        <tr>
          <td>1</td>
          <td>HTML</td>
          
        </tr>
        <tr>
          <td>2</td>
          <td>Css</td>
        </tr>
        <tr>
          <td>3</td>
          <td>JavaScript</td>
        </tr>
        <tr>
          <td>4</td>
          <td>React</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Node.js</td>
        </tr>
      </table>
    </div>
  )
}

export default Home