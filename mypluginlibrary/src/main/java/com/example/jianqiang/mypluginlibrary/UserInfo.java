package com.example.jianqiang.mypluginlibrary;

import java.io.Serializable;

/**
 * Created by jianqiang on 17/1/11.
 */
public class UserInfo implements Serializable {
    public String userName;
    public int score;

    public UserInfo(String userName, int score) {
        this.userName = userName;
        this.score = score;
    }
}
