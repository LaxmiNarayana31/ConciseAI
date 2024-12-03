import Demo from "./components/Demo";
import IntroSection from "./components/IntroSection";
import "./App.css";

const App = () => {
  return (
    <main>
      <div className="main">
        <div className="gradient" />
      </div>

      <div className="app">
        <IntroSection />
        <Demo />
      </div>
    </main>
  );
};

export default App;
