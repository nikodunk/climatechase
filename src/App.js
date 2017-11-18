import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import $ from 'jquery'; 

class App extends Component {

  onError(error){
    console.log(error)
  }

  constructor(props) {
    super(props);

    this.state = {  results: {
                        gdp: 1000000,
                        gdpgrowth: 5,
                        funds: 100000
                          }
                  }
      
  }

  componentDidMount() {
    // $.get("http://localhost:5000/", function(result){
    //         console.log('the backend just sent you this:' + result )
    //      })
    console.log(this.state)
    $.get("http://localhost:5000/", function(result){
        console.log('the backend just sent you this:' + result )
            this.setState({results: result});
            console.log(this.state.results);
     })
  } 

  onClick(e){
    console.log('sending this to backend: +1 ' + e.target.id + ' clicked')
    $.post("http://localhost:5000/", this.state.input)
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" /><h1 className="App-title">ClimateChase</h1>
        </header>
        <h1 className="subtitle">
          GDP: {this.state.results.gdp}<br />
          Growth: {this.state.results.gdpgrowth}%
        </h1>
        <button onClick={this.onClick.bind(this)} id="wind">invest in windpower tech</button>
        <button onClick={this.onClick.bind(this)} id="solar">invest in solar tech</button>
      </div>
    );
  }

  
}

export default App;