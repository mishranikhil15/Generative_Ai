import logo from './logo.svg';
import './App.css';
import Hello from './component/Hello';
import Counter, { Print } from './component/Counter';

function App() {
  return (
    <div className="App">
    <Hello />
    <Counter />
    <Print />

    </div>
  );
}

export default App;
