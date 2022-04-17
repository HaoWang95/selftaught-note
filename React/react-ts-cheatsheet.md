# ** Use React with TypeScript**

```TypeScript
type SthProps = {
    message? : string;
}

// easist approach to declare a functional component
const Component = ({message}: SthProps) => <div>{message}</div>

// declare a return type
const Component = ({message}: SthProps): JSX.Element => <div>{message}</div>

// incline type declaration;
const Component = ({message}: {message?: string}): JSX.Element => <div>{message}</div> 
```

## React.FC is discouraged.
There're tons of examples like:
```TypeScript
type SthProps = {
    message: string;
}

const Component: React.FunctionalComponent<SthProps> = ({message}) => (<div>{message}</div>);
```
>- Consider using **`React.VFC`** to replace React.FC

##