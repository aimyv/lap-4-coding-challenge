import { Home, NotFound } from './pages';
import { Header, Footer } from './layouts';
import urlAPI from './components/urlAPI';
import './App.css';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/*" element={<NotFound/>}></Route>
      </Routes>
      <urlAPI />
      <Footer/>
    </div>
  );
}

export default App;
