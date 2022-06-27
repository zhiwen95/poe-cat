import ReactDOM from "react-dom/client";
import {
    HashRouter,
    Routes,
    Route,
} from "react-router-dom";
import About from './About';
import App from './App';
// import your route components too

const root = ReactDOM.createRoot(
    document.body
);
root.render(
    <HashRouter>
        <Routes>
            <Route path="/" element={<App />}>
            </Route>
            <Route path="/about" element={<About />} />
        </Routes>
    </HashRouter>
);
