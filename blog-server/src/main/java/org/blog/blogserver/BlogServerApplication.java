package org.blog.blogserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.SpringServletContainerInitializer;

@SpringBootApplication(
		exclude = {SecurityAutoConfiguration.class},
		scanBasePackages = {"org.blog.blogserver"}
)
public class BlogServerApplication extends SpringServletContainerInitializer {

	public static void main(String[] args) {
		SpringApplication.run(BlogServerApplication.class, args);
	}
}
