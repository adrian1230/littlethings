// Learn more about F# at docs.microsoft.com/dotnet/fsharp
(* this is a block comment *)

open System

// Define a function to construct a message to print
let from whom =
    sprintf "from %s" whom

[<EntryPoint>]
let main argv =
    let result = 1 + 2
    let message = from "F#" // Call the function
    printfn "Hello world %s %d" message result
    0 // return an integer exit code