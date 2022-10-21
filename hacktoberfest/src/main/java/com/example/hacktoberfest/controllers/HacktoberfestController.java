package com.example.hacktoberfest.controllers;

import java.util.HashMap;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HacktoberfestController {
    @GetMapping("/health")
    public Map<String,String> getHealth(){
        Map<String,String> map = new HashMap<>();
        map.put("status", "OK");
        return map;
    }
}
