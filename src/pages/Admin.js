import React from 'react';
import { Layout, Menu, Icon, Input, Button, List, Tag } from 'antd';
import './Admin.css';
import { PUBLIC_URL } from '../constants';

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

export default class Admin extends React.Component {
    state = {
        initLoading: true,
        loading: false,
        list: []
    }

    async componentDidMount() {
        const res = await fetch(`${PUBLIC_URL}/mock/people.json`);
        const data = await res.json();

        this.setState({
            initLoading: false,
            list: data,
        });
    }

    render() {
        const { initLoading, list } = this.state;

        return (
            <Layout>
                <Header className="header">
                    <div className="logo" />
                    <Menu
                        theme="dark"
                        mode="horizontal"
                        defaultSelectedKeys={['2']}
                        style={{ lineHeight: '64px' }}
                    >
                        <Menu.Item key="1">不可思道书店后台管理系统</Menu.Item>
                    </Menu>
                </Header>
                <Content style={{ padding: '0 50px' }}>
                    <Layout style={{ padding: '24px 0', background: '#fff' }}>
                        <Sider width={200} style={{ background: '#fff' }}>
                            <Menu
                                mode="inline"
                                defaultSelectedKeys={['1']}
                                defaultOpenKeys={['sub1']}
                                style={{ height: '100%' }}
                            >
                                <SubMenu
                                    key="sub1"
                                    title={
                                        <span>
                                            <Icon type="user" />
                                            会员管理
                </span>
                                    }
                                >
                                    <Menu.Item key="1">会员检索</Menu.Item>
                                    <Menu.Item key="2">添加会员</Menu.Item>
                                    <Menu.Item key="3">删除会员</Menu.Item>
                                    <Menu.Item key="4">更新会员</Menu.Item>
                                </SubMenu>
                                <SubMenu
                                    collapsible={false}
                                    key="sub2"
                                    title={
                                        <span>
                                            <Icon type="laptop" />
                                            图书管理
                </span>
                                    }
                                >
                                    <Menu.Item key="5">图书检索</Menu.Item>
                                    <Menu.Item key="6">添加图书</Menu.Item>
                                    <Menu.Item key="7">删除图书</Menu.Item>
                                    <Menu.Item key="8">更新图书</Menu.Item>
                                </SubMenu>
                                <SubMenu
                                    key="sub3"
                                    title={
                                        <span>
                                            <Icon type="notification" />
                                            订单管理
                </span>
                                    }
                                >
                                    <Menu.Item key="9">订单检索</Menu.Item>
                                    <Menu.Item key="10">添加订单</Menu.Item>
                                    <Menu.Item key="11">删除订单</Menu.Item>
                                    <Menu.Item key="12">更新订单</Menu.Item>
                                </SubMenu>
                            </Menu>
                        </Sider>
                        <Content style={{ padding: '0 24px', minHeight: 280 }}>
                            <Input className='search-input' placeholder='根据关键词查询会员信息，回车以搜索' />
                            <Button style={{ position: 'absolute', top: 88, right: 80 }}>搜索</Button>
                            <List style={{ marginTop: 30 }}
                                className='user-list'
                                loading={initLoading}
                                itemLayout="horizontal"
                                dataSource={[{}]}
                                renderItem={() => (
                                    <List.Item style={{ display: 'flex', justifyContent: 'center', width: 800, margin: '0 auto' }}>
                                    <span style={{ marginLeft: 0, width: 200 }}>会员号</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>用户名</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>用户邮箱</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>用户类型</span>
                                    </List.Item>
                                )}
                            />
                            <List
                                className='user-list'
                                loading={initLoading}
                                itemLayout="horizontal"
                                dataSource={list}
                                renderItem={({ id, name, type, email }) => (
                                    <List.Item style={{ display: 'flex', justifyContent: 'center', width: 800, margin: '0 auto' }}>
                                    <span style={{ marginLeft: 0, width: 200 }}>{ id }</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>{ name }</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>{ email }</span>
                                    <span style={{ marginLeft: 0, width: 200 }}>{ 
                                        type === '管理员' ? (<Tag color="geekblue">管理员</Tag>) : (<Tag color="blue">会员</Tag>)
                                    }</span>
                                    </List.Item>
                                )}
                            />
                        </Content>
                    </Layout>
                </Content>
                <Footer style={{ textAlign: 'center', marginTop: -25 }}>
                    <p>©2019 Created by 数据课设第1小组</p>
                </Footer>
            </Layout>
        )
    };
}