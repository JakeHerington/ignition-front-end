import { Navbar, Nav, NavDropdown } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

export default function NavBar() {

    return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" fixed="top">
        <Navbar.Brand href="#home">Solar Farm</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="">Alarms</Nav.Link>
                <Nav.Link href="">Trends</Nav.Link>
                <NavDropdown title="Site" id="collasible-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Panel 1</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Panel 2</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Panel 3</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.4">Weather Sensor</NavDropdown.Item>
                </NavDropdown>
                <Nav.Link href="">Reports</Nav.Link>
            </Nav>
        </Navbar.Collapse>
    </Navbar>
    )
}