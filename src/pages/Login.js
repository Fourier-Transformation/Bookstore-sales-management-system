import React from 'react';
import styled from 'styled-components';

export default class Login extends React.Component {
    render() {
        return (
            <StyledLoginPanel>
                <div>用户名: 
                    <input type='text' name='username'></input>
                </div>
                <div>密码: 
                    <input type='password' name='password'></input>
                </div>
                <button sr></button>
            </StyledLoginPanel>
        );
    }
}

const StyledLoginPanel = styled.div`
    box-shadow: 0 0 0 20px #666666;
    max-width: 600px;
    margin: 200px auto;
    padding: 10px;
`;