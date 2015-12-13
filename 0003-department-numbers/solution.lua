
function departments()
  for z=2,6,2 do
    for y=1,7 do
      if y ~= z then
        x = 12 - y - z
        if x >=1 and x <= 7 and x ~= y and x ~= z then
          print(x, y, z)
        end
      end
    end
  end
end

departments()
