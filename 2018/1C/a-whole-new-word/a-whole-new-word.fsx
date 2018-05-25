// https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard
// A Whole New Word
// Vincent and Desta are childhood friends. Today, Vincent is showing N distinct L-letter words to Desta by using some letter tiles. Each tile contains one uppercase English alphabet letter, and one number between 1 and L. A word consists of the letters spelled out by L tiles with numbers from 1 through L, in order. (Vincent's words are not necessarily real English words.)

// Cartesian product of lists
let product lists = 
    let folder list state =
         state |> Seq.allPairs list |> Seq.map List.Cons 
    Seq.singleton List.empty |> List.foldBack folder lists

// repeat sequence indefinitely
let cycle seq =
    Seq.initInfinite (fun _ -> seq) |> Seq.concat

let T = System.Console.ReadLine() |> int
for case in [1..T] do
    let N = System.Console.ReadLine().Split() |> Array.map int |> Array.head
    let words = [1..N] |> List.map (fun _ -> System.Console.ReadLine()) |> List.sort
    let letter i (w:string) = w.[i]
    let ithLetters i = words |> List.map (letter i)
    let L = words.[0].Length
    let letters = [0..L-1] |> List.map (ithLetters >> List.sort >> List.distinct)
    let feasibleWords = letters |> product |> Seq.map (Seq.toArray >> System.String)
    let newWord = feasibleWords |> Seq.zip (cycle words) |> Seq.tryFind (fun (a,b) -> a <> b) |> Option.map snd
    let solution = newWord |> Option.defaultValue "-"
    printfn "Case #%d: %s" case solution
