export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <h2>
        <span className="bg-red-500 p-1 text-black font-bold">
          Authentication layout
        </span>
      </h2>

      {/* чак сега се вклчюва останалото съдържание */}
      {children}
    </div>
  );
}
