# Assets 

Datsets is a folder dedicated for datasets, they should follow a schema 

right now something like:
```
{
  paths: string[];
  groups: Record<string, string[]>;
}
```

where results is a record collection (Set) of paths that each image path point to what collection they would belong too.