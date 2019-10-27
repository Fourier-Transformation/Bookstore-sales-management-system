import React from 'react';
import styled from 'styled-components';
import { STORE_NAME } from '../constants';
import { Link } from 'react-router-dom';

export default class TopBar extends React.Component {
    render() {
        return (
            <StyledTopBar>
                <span>欢迎光临{ STORE_NAME }书店, 请
                    <Link to='/login' className='login'>登录</Link> | 
                    <Link className='be-member'> 成为会员</Link> | 
                    <Link to='/admin' className='admin-login-button'>管理员</Link>
                </span>
            </StyledTopBar>
        );
    }
}

const StyledTopBar = styled.div`
    height: 34px;
    background: #f9f9f9;

    * {
        font-size: 14px;
        line-height: 34px;
    }

    a { text-decoration: none; }
    a.login {
        color: red;
    }
    a.be-member {
        color: black;
        &:hover {
            color: red;
        }
    }
`;