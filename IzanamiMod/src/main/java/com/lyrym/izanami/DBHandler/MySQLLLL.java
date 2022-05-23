package com.lyrym.izanami.DBHandler;

import com.mysql.jdbc.Driver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MySQLLLL {

    private Connection conn;

    public MySQLLLL() throws SQLException {
        DriverManager.registerDriver (new Driver());
    }

    public void connect(String host, int port, String database, String user, String password) {

        if(!isConnected()){
            try {
                conn = DriverManager.getConnection("jdbc:mysql://" + host + ":" + port + "/" + database, user, password);
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public void disconnect(){
        if(isConnected()){
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public boolean isConnected(){
        try {
            if((conn == null) || (conn.isClosed()) || conn.isValid(5)){
                return false;
            }
            return true;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }


    public Connection getConnection() {
        return conn;
    }
}
