import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import TopBar from './components/TopBar';
import Header from './containers/Header';
import Categories from './components/Categories'
import BookList from './containers/BookList';
import BookDetail from './components/BookDetail';
import LoginPage from './pages/Login';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route exact path='/'>
              <TopBar />
              <Header />
              <Categories />
              <BookList />
            </Route>
            <Route exact path='/bookdetail'>
              <TopBar />
              <BookDetail />
            </Route>
            <Route>
              <LoginPage />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
