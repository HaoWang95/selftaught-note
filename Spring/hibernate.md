# **Hibernate**

Hibernate is included as one of the default dependencies in spring jpa.

Because database schema is driven by SQL standard, while the domain model comes with object-oriented.

### Hibernate hbm2ddl.auto schema generation
The `hibernate.hbm2ddl.auto` configuration property is used to customize the Hibernate database schema generation process.
* **none** -> Diables the hbm2.ddl.auto tool. Hibernate is not going to take any actions for managing the underlying database schema.
* **create-only** -> Instructs Hibernate to generate the database schema from the entity model.
* **drop** -> Inscructs Hibernate to drop the database schema using the entity model as a reference for the DDL DROP statements.
* **create** -> Instructs Hibernate the drop the database schema and recreate it afterward using the entity model as a reference. Upon closing the JPA EntityManagerFactory or the Hibernate SessionFactory, the database schema will be dropped again.
* **validate** -> Instructs Hibernate to validate the underlying database schema against the entity mappings.
* **update** -> Instructs Hibernate to update the database schema by comparing the existing schema with the entity mappings and generate schema migration scripts.
For none, if we want to create the schema manually, then we just don't set the hbm2ddl.auto configuration property because the default schema generation strategy is none.
For update, this option should be avoided as we need to handle the schema migrations with a tool like **Flyway**.
If we are using a schema migration tool like **Flyway**, and want to generate the initial migration script from the JPA and Hibernate entities, we should use `create-only` and `drop` options and **`log the auto-generated SQL statements`** in order to extract the DDL statements.
The `create` and `create-drop` options make senses for the Hibernate core integration tests but are not suitable for an end-user project because we should use the same schema migration scripts we are using for the production system in order to generate the database schema for running the integration tests.

#### The JPA schema generation options
The hibernate-specific hibernate.hbm2ddl.auto configuration can be standardized by JPA via the following settings.
* **javax.persistence.schema-generation.database.action**
* **javax.persistence.schema-generation.scripts.action**
The **`javax.persistence.schema-generation.database.action`** configuration tells Hibernate **whether to apply the schema migration against the underlying database upon bootstrapping the EntityManagerFactory.**
The **`javax.persistence.schema-generation.scripts.action`** configurartion tells Hibernate whether to generate the schema migration DDL statements to an external file. The CREATE DDL statements are written to the file given by the `javax.persistence.schema-generation.scripts.create-target` configuration property while the DROP DDL statements are written to the file given by the `javax.persistence.schema-generation.scripts.drop-target` configuration property.

Values taken by **`javax.persitence.schema-generation.database.action`** and **`javax.persistence.schema-generation.scripts.action`**:
* none -> default option, it disables the schema generation tool.
* create -> Instructs Hibernate to generate the database schema from the entity model. It's equivalent to the create-only hibernate.hbm2ddl.auto strategy.
* drop -> Equivalent to the `drop hibernate.hbm2ddl.auto` strategy.
* drop-and-create -> Instructs Hibernate to drop the database schema and recreate it afterward using the entity model as a reference. Equivalent to `create hibernate.hbm2ddl.auto` strategy.

*FetchType.EAGER* might choose a SQL join or a secondary select whether the entity is fetched directly from EntityManager or through a JPQL or a Creteria API query.

*SQL injection prevention* Hibernate uses PreparedStatement by default. It protects against SQL injection, but the data access layer can better take advantage of server-side and client-side statement caching as well.

*Monitoring connections* FlexyPool, DataSource Proxy. Hibernate has a built in statistics collector.(Disabled by default)

## Types


Mapping inheritance in a relational database is one of the most obvious object-relational impedance mismatches.
> - Single Table Inheritance, which uses a single database table to represent all classes in a given inheritance hierarchy.
> - Class Table Inheritance, which maps each class to a table, and the inheritance association is resolved through table joins.
> - Concrete Table Inheritance, where each table defines all fields that are either defined in subclasses or inherited from a superclass.

The strategies of JPA:
> - InheritanceType.SINGLE_TABLE
> - InheritanceType.JOINED
> - InheritanceType.TABLE_PER_CLASS.

Single table inheritance is the default JPA strategy.
One of the advantage of using inheritance in the Domain Model is the support of the polymorphic queries. When the application developer issues a select query against the entity.


## @OneToOne 
* **@OneToOne** using shared primary key
```java

@Entity(name = "authors")
public class Author{
    
}
```

#### EntityManager
EntityManager.flush() will force the data to be persist in the database immediately as EntityManager.persist() will not.
When we call em.persist(), we only makes the entity get managed by the `EntityManager` and adds the entity instance to the **`Persistence Context`**. An explicit flush will make the entity now residing in the **`Persistent Context`** to be moved to the db(which means the flush will execute sql in the db).

em.remove(Object entity) means remove the entity instance, the database is affected right away. While em.detatch(Object entity) will remove the given entity from the **`Persistent context`**

