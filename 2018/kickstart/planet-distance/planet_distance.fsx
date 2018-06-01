// https://code.google.com/codejam/contest/4384486/dashboard#s=p0
"""There are N planets in the universe, and Google's Space division has installed N vacuum tubes through which you can travel from one planet to another. The tubes are bidirectional; travelers may use a tube between two planets to travel from either of those planets to the other. Each vacuum tube connects two planets and no two vacuum tubes connect the same pair of planets. These tubes connect the planets such that it is possible to travel from any planet to any other planet using one or more of them. Some of these tubes are connected such that there exists exactly one cycle in the universe. Google has hidden gifts in all the planets that are part of this cycle. Now, Google wants to know how far away each of the planets in the universe is from the gifts.
Your task is to find the minimum distance (in terms of the number of vacuum tubes) between each planet and a planet that is part of the cycle. Planets that are part of the cycle are assumed to be at distance 0."""

let solveByBacktracking moves solved initialState = 
    let rec inner state = 
        match state with
            | Some progress when (progress |> solved |> not) ->
                progress |> moves |> Seq.map (Some >> inner) |> Seq.tryFind Option.isSome |> Option.flatten
            | _ -> state
    initialState |> Some |> inner

let findCycle edges = 
    let solved path =
        match path with
        | v::_::rest ->
            let seen x = rest |> List.contains x
            edges |> Array.item v |> List.exists seen
        | _ -> false

    let moves path = 
        let n = edges |> Array.length
        let novel x = path |> List.contains x |> not
        let prepend x = x::path
        match path with
        | v::_ -> edges.[v] |> Seq.where novel |> Seq.map prepend
        | [] -> [0..n-1] |> Seq.map List.singleton

    let pathWithCycle = [] |> solveByBacktracking moves solved
    let fix path = 
        let v = path |> List.head
        let neighbours = edges |> Array.item v
        let seen x = neighbours |> List.contains x
        let i = path |> List.tryFindIndexBack seen
        path.GetSlice (Some 0, i)

    pathWithCycle |> Option.map fix


let T = System.Console.ReadLine() |> int
for case in [1..T] do
    let N = System.Console.ReadLine() |> int
    let edges = [|for _ in [1..N] -> []|]
    for _ in [1..N] do
        let edge = System.Console.ReadLine().Split() |> Array.map (int >> (+) (-1))
        let v, w = Array.head edge, Array.last edge
        edges.[v] <- w::edges.[v]
        edges.[w] <- v::edges.[w]

    let rec bfs found = 
        // printfn "found %A" found
        match found with 
        | []::_ -> found
        | last::_ ->
            let seen = found |> List.collect id
            let novel x = seen |> List.contains x |> not
            let next = last |> List.collect (fun v -> Array.item v edges) |> List.where novel
            next::found |> bfs
        | [] -> invalidArg "found" "should not be empty"

    let cycle = edges |> findCycle |> Option.get

    // edges |> printfn "edges %A"
    // cycle |> printfn "cycle %A"

    let byDistance = [cycle] |> bfs |> List.rev
    // byDistance |> printfn "distances %A"
    
    let distance x = 
        byDistance |> List.findIndex (List.contains x)
    let distances = [0..N-1] |> List.map distance
    let solution = System.String.Join(" ", distances)
    printfn "Case #%d: %s" case solution
