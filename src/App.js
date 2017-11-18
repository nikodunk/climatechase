import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import $ from 'jquery'; 

class App extends Component {

  componentDidMount() {
    $.getJSON("http://localhost:5000/data.json", function(result){
            console.log('this works and is the JSON:' + result )
         })
  } 



  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="subtitle">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }

  
}

export default App;