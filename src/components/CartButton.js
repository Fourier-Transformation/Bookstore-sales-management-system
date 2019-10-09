import React from 'react';
import styled from 'styled-components';

export default class CartButton extends React.Component {
    state = {
        count: 0
    }

    add() {
        this.setState({
            count: this.state.count++
        })
    }

    dec() {
        this.setState({
            count: this.state.count--
        })
    }

    render() {
        return (
            <Button onclick={ () => { Math.random() > 0.5 ? this.add() : this.dec() } }>
                { this.state.count }
            </Button>
        );
    }
}

const Button = styled.button`

`;