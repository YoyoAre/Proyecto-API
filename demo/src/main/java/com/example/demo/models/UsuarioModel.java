package com.example.demo.models;
//import javax.persistence.*;
import jakarta.persistence.*;

@Entity
@Table(name = "usuario")
public class UsuarioModel{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(unique = true,nullable= false)
    private Long id;
    private String nombre;

    public void setId(Long id){
        this.id = id;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public Long getId(){
        return id;
    }
    public String getNombre(){
        return nombre;
    }
}
