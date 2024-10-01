import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import { Link } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import { Button, Box } from '@mui/material';
import './Navbar.css';

const Navbar = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: '#448f97' }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Historical Treasury Yields
          </Typography>

          <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">Yields</Button>
          </Link>

          <Link to="/orders" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">Orders</Button>
          </Link>

          <Link to="/new-order" style={{ textDecoration: 'none', color: 'inherit' }}>
            <Button color="inherit">New Order</Button>
          </Link>

        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Navbar;

