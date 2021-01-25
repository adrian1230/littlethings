// Learn more about F# at docs.microsoft.com/dotnet/fsharp
(* this is a block comment *)

open System

// Define a function to construct a message to print
let from whom =
    sprintf "from %s" whom

let con which = 
    sprintf "%s" which

let devour = 
    let jo = @"<room number=""1001"">"
    let oj = """<id number="1092">"""
    sprintf "%s %s" jo oj

let negate x = x * -1
let plus x = x + x

[<EntryPoint>]
let main argv =
    let result = 1 + 2
    let msg = con "Babe"
    let message = from "F#" // Call the function
    printfn "Hello world %s %d %s" message result msg
    let txt = 5
    let txt1 = 5.18
    printfn "%d %f" txt txt1
    printfn "%s" devour
    printfn "The\n\
            One\n\
            and only"
    // val a : byte = 86uy
    // val b : int = 86
    // val c : int64 = 86L
    let a,b,c = 86uy, 86, 86L
    printfn "%d %d %d" a b c
    printfn "%d" (negate (plus 5))
    0 // return an integer exit code