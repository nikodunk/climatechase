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

    this.state = {
        'Money': 'test',
        'Emissions Per Year (GHP)': 200,
        'Start_Year': 2017,
        'Curr_Year': 2017,
        'Solar_Investment': 0,
        'Wind_Investment': 0,
        'Nuclear_Investment': 0,
        'Gas_Investment': 0,
        'GDP': 18566900000000,
        'Sea_Levels': 0,
        'Electricity_Price': 0,
        'Probability_of_violence': 0,
        'Agriculture': 0,
        'Risk_of_Hurricane': 0,
        'Game_Over': false
    }
      
  }

  componentDidMount() {

    this.getRequest()
    
  }

  getRequest(){
      var test
      $.get("http://localhost:5000/", function(result){
            console.log('the backend just sent you this:' + result )
            test = result
            console.log(result);
     })
      this.setState(test)
      console.log(test)
   }





  onClick(e){
    console.log(e.target.id)
    $.post("http://localhost:5000/" + e.target.id, e.target.id)
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" /><h1 className="App-title">ClimateChase</h1>
        </header>
        <h1 className="subtitle" id="GDP"> GDP: ${this.state.GDP} </h1>
        <h1 className="subtitle" id="GDP"> GDP: ${this.state.GDP} </h1>
        <h1 className="subtitle" id="Year">{this.state.Curr_Year} </h1>
        <h1 className="subtitle" id="Year">Finances: ${this.state.Money} </h1>
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