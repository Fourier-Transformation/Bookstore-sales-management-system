import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import CommonHeader from './containers/CommonHeader';
import TopBar from './components/TopBar';
import BookList from './containers/BookList';
import BookDetail from './components/BookDetail';
import LoginPage from './pages/Login';
import Payment from './containers/Payment';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route exact path='/'>
              <CommonHeader />
              <BookList />
            </Route>
            <Route exact path='/bookdetail'>
              <TopBar />
              <BookDetail />
            </Route>
            <Route exact path='/payment'>
              <CommonHeader />
              <Payment />
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
