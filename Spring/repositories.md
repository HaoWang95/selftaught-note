This note will include __CrudRepository__, __JpaRepository__ and __PagingAndSortingRepository__.

The **JpaRepository** extends the **PagingAndSortingRepository**.

'''java

public interface JpaRepository<T, ID> extends PagingAndSortingRepository<T, ID>, QueryByExampleExecutor<T> {}


The **PagingAndSortingRepository** extends the **CrudRepository**. 

That means for our repositories, extend to **JpaRepository** will make them contain the full API of both **PagingAndSortingRepository** and **CrudRepository**.

