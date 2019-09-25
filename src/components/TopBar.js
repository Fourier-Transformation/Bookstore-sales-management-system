import React from 'react';
import styled from 'styled-components';
import { STORE_NAME } from '../constants';

export default class TopBar extends React.Component {
    render() {
        return (
            <StyledTopBar>
                <span>欢迎光临{ STORE_NAME }, 请<a className='login'>登录</a> <a className='be-member'>成为会员</a></span>
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