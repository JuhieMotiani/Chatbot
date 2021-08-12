import './App.css';
import Home from '../src/Components/Home/Home';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/' component={Home}></Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
