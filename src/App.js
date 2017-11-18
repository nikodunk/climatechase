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

    this.state = {  results: {  budget: 10,
                                gdp: 100,
                                gdpgrowth: 5,
                                year: 2010},
                    time: 2010
                  }
      
  }

  componentDidMount() {
    $.get("http://localhost:5000/", function(result){
        console.log('the backend just sent you this:' + result )
            this.setState({results: result});
            console.log(this.state.results);
     })
    setInterval(function() {this.setState({time: this.state.time + 1})}.bind(this), 500)
  } 





  onClick(e){
    console.log('sending this to backend: +1 ' + e.target.id + ' clicked')
    var updatedResults = this.state.results
    updatedResults.budget = updatedResults.budget - 1
    this.setState({results: updatedResults})
    $.post("http://localhost:5000/", this.state.input)
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" /><h1 className="App-title">ClimateChase</h1>
        </header>
        <h1 className="subtitle"> GDP: ${this.state.results.gdp} </h1>
        <h1 className="subtitle"> Growth: {this.state.results.gdpgrowth}% </h1>
        <h1 className="subtitle"> Budget: ${this.state.results.budget}</h1>
        <h1 className="subtitle"> Date: {this.state.time}</h1>
        invest<br />
        <button onClick={this.onClick.bind(this)} id="wind">$1=>windpower</button><br />
        <button onClick={this.onClick.bind(this)} id="solar">$1=>solar</button><br />
        <button onClick={this.onClick.bind(this)} id="nuclear">$1=>nuclear</button><br />
        <button onClick={this.onClick.bind(this)} id="fossil">$1=>fossil</button><br />
      </div>
    );
  }

  
}

export default App;