import { useState } from "react";


export function Print(){
    return <h1>Print</h1>
}

 function Counter() {
  const [count, setCount] = useState(0);

   function Inc(){
    setCount(count+1)
   }

   function Dec(){
    if(count<1){
        alert("Cannot decrease furthur");
        return
    }
    setCount(count-1)
   }

  return (
    <div>
      <button onClick={Inc}>+</button>
      <h1>Count{count}</h1>
      <button onClick={Dec}>-</button>
    </div>
  );
}

export default Counter