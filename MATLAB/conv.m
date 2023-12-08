function[] = conv(input, output, tomono)

[x, Fs] = audioread(input);

if (tomono == 1)
    y = x(:,1);
    writematrix(y, output);
else
    writematrix(x, output);

end