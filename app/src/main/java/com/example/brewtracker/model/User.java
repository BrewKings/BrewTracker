package com.example.brewtracker.model;

public class User {
    private String userId;
    private static final User user = new User();
    private User(){
      
    }
    public User getInstance(){
        return user;
    }
}
