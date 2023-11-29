import logo from './logo.svg';
import './App.css';
import Navbar from './Navbar.js';
import Content from './Content.js';
import Services from './Services.js';
import SkillsBar from './SkillsBar.js';
import Projects from './Projects.js';
import Footer from './Footer.js';


export default function App() {
  return <div className="container cover-page">
            <Navbar />
            <Content />
            <SkillsBar />
            <Services />
            <Projects />
            <Footer />
          </div>
}
