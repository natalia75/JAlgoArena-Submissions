package com.jalgoarena

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.cache.annotation.EnableCaching
import org.springframework.cloud.netflix.eureka.EnableEurekaClient
import org.springframework.context.annotation.Bean
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;


@SpringBootApplication
@EnableEurekaClient
@EnableSwagger2
@EnableCaching(proxyTargetClass=true)
open class JAlgoArenaSubmissionsApp

fun main(args: Array<String>) {
    SpringApplication.run(JAlgoArenaSubmissionsApp::class.java, *args)
}

@Bean
fun api(): Docket = Docket(DocumentationType.SWAGGER_2)
        .select() 
        .apis(RequestHandlerSelectors.basePackage("com.jalgoarena.web"))
        .paths(PathSelectors.any())                          
        .build()