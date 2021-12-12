# **Hibernate**

Hibernate is included as one of the default dependencies in spring jpa.

Because database schema is driven by SQL standard, while the domain model comes with object-oriented.

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