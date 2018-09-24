package org.blog.blogserver.controller;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.blog.blogserver.entity.User;
import org.blog.blogserver.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("user-mangement")
public class UserController {

    private static final Logger logger = LogManager.getLogger(UserController.class);

    private final UserRepository userRepository;

    @Autowired
    public UserController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @GetMapping(value = "users")
    private List<User> findAll(){
        logger.info("start find all");
        List<User> target = new ArrayList<>();
        userRepository.findAll().forEach(target::add);
        logger.info("end find all");
        return target;
    }

}
