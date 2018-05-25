// Cartesian product of lists
let product lists = 
    let folder list state =
         state |> Seq.allPairs list |> Seq.map List.Cons 
    Seq.singleton List.empty |> List.foldBack folder lists

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
    let solution = Option.defaultValue "-" newWord
    printfn "Case #%d: %s" case solution
